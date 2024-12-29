import { useState, useEffect } from 'react';

const TodoListPage = ({ username }) => {
  const [todos, setTodos] = useState([]);
  const [isCreateOpen, setIsCreateOpen] = useState(false);
  const [isEditOpen, setIsEditOpen] = useState(false);
  const [currentTodo, setCurrentTodo] = useState(null);
  const [newContent, setNewContent] = useState('');
  const [error, setError] = useState('');

  const fetchTodos = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/todo/read?username=${username}`);
      const data = await response.json();
      setTodos(data);
    } catch (err) {
      setError('Failed to fetch todos');
    }
  };

  useEffect(() => {
    fetchTodos();
  }, [username]);

  const handleCreate = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/todo/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, content: newContent })
      });

      if (response.ok) {
        setNewContent('');
        setIsCreateOpen(false);
        fetchTodos();
      } else {
        setError('Failed to create todo');
      }
    } catch (err) {
      setError('Network error occurred');
    }
  };

  const handleUpdate = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/todo/update', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          content_id: currentTodo.content_id,
          content: newContent
        })
      });

      if (response.ok) {
        setNewContent('');
        setIsEditOpen(false);
        setCurrentTodo(null);
        fetchTodos();
      } else {
        setError('Failed to update todo');
      }
    } catch (err) {
      setError('Network error occurred');
    }
  };

  const handleDelete = async (contentId) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/todo/delete', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          content_id: contentId
        })
      });

      if (response.ok) {
        fetchTodos();
      } else {
        setError('Failed to delete todo');
      }
    } catch (err) {
      setError('Network error occurred');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-2xl mx-auto">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Todo List</h2>
          <button
            onClick={() => setIsCreateOpen(true)}
            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
          >
            Create New
          </button>
        </div>

        {error && <div className="text-red-500 mb-4">{error}</div>}

        <div className="space-y-4">
          {todos.map(todo => (
            <div key={todo.id} className="bg-white p-4 rounded-lg shadow flex justify-between items-center">
              <span>{todo.content}</span>
              <div className="space-x-2">
                <button
                  onClick={() => {
                    setCurrentTodo(todo);
                    setNewContent(todo.content);
                    setIsEditOpen(true);
                  }}
                  className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(todo.content_id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Create Todo Modal */}
        {isCreateOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white p-6 rounded-lg w-96">
              <h3 className="text-xl font-bold mb-4">Create New Todo</h3>
              <input
                type="text"
                value={newContent}
                onChange={(e) => setNewContent(e.target.value)}
                className="w-full mb-4 p-2 border rounded"
                placeholder="Todo content"
              />
              <div className="flex justify-end space-x-2">
                <button
                  onClick={() => setIsCreateOpen(false)}
                  className="bg-gray-200 px-4 py-2 rounded hover:bg-gray-300"
                >
                  Cancel
                </button>
                <button
                  onClick={handleCreate}
                  className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
                >
                  Create
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Edit Todo Modal */}
        {isEditOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white p-6 rounded-lg w-96">
              <h3 className="text-xl font-bold mb-4">Edit Todo</h3>
              <input
                type="text"
                value={newContent}
                onChange={(e) => setNewContent(e.target.value)}
                className="w-full mb-4 p-2 border rounded"
                placeholder="Todo content"
              />
              <div className="flex justify-end space-x-2">
                <button
                  onClick={() => {
                    setIsEditOpen(false);
                    setCurrentTodo(null);
                  }}
                  className="bg-gray-200 px-4 py-2 rounded hover:bg-gray-300"
                >
                  Cancel
                </button>
                <button
                  onClick={handleUpdate}
                  className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                >
                  Update
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};


export default TodoListPage;