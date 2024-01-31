import React from 'react';
import AuthForm from '../components/AuthForm';

const LoginPage = () => {
  const handleSubmit = (formData) => {
    console.log('Form data:', formData);
    // Здесь вы можете добавить логику для отправки данных на сервер
  };

  return (
    <div>
      <h1>Login Page</h1>
      <AuthForm onSubmit={handleSubmit} />
    </div>
  );
};

export default LoginPage;
