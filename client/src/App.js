import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import TodoListPage from './components/TodoList';
import LoginPage from './components/Login';
import SignupPage from './components/Signup';

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState('');

  return (
    <Router>
      <Routes>
        <Route 
          path="/login" 
          element={
            <LoginPage 
              setIsAuthenticated={setIsAuthenticated} 
              setUsername={setUsername} 
            />
          } 
        />
        <Route path="/signup" element={<SignupPage />} />
        <Route 
          path="/todos" 
          element={
            isAuthenticated ? (
              <TodoListPage username={username} />
            ) : (
              <Navigate to="/login" replace />
            )
          } 
        />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </Router>
  );
};

export default App;