// Хотел стили накинуть, но они не работают, но принял решение, что нужно показать, что технически могу

import React, { useState } from 'react';

const AuthForm = ({ onSubmit, isRegistering }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formData = { username, password };
      if (isRegistering) {
        // Здесь еще не совсем разобрался, что у меня происходит с почтой, но как бы работает
        formData.email = email;
      }
      const response = await fetch(`http://127.0.0.1:8000/api/${isRegistering ? 'register' : 'token'}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        throw new Error('Ошибка при регистрации пользователя.');
      }
      const data = await response.json();
      onSubmit(data.access);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col items-center">
      {error && <p className="text-red-500">{error}</p>}
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="mb-4 p-2 border border-gray-300 rounded w-64"
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="mb-4 p-2 border border-gray-300 rounded w-64"
      />
      {isRegistering && (
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="mb-4 p-2 border border-gray-300 rounded w-64"
        />
      )}
      <button type="submit" className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded">
        {isRegistering ? 'Зарегистрироваться' : 'Войти'}
      </button>
    </form>
  );
};

export default AuthForm;