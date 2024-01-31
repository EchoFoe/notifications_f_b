import React, { useState } from 'react';
import AuthForm from './AuthForm';
import Cookies from 'js-cookie';

const AuthContainer = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);

  const handleAuthSubmit = (accessToken) => {
    console.log('Полученный токен:', accessToken);
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    Cookies.remove('access_token');
    console.log('Полученный токен удален');
    setIsLoggedIn(false);
  };

  const handleRegister = () => {
    setIsRegistering(true);
  };

  const handleViewStats = () => {
    // В этом обработчике я хотел бы делать статистику уведомлений на фронте
  };

  return (
    <div>
      {!isLoggedIn ? (
        <div>
          <h2>{isRegistering ? 'Регистрация' : 'Авторизация'}</h2>
          <AuthForm onSubmit={handleAuthSubmit} isRegistering={isRegistering} />
          <p>
            {!isRegistering ? (
              <span>
                Нет аккаунта?{' '}
                <button onClick={handleRegister}>Зарегистрироваться</button>
              </span>
            ) : (
              <span>
                Уже есть аккаунт?{' '}
                <button onClick={() => setIsRegistering(false)}>Войти</button>
              </span>
            )}
          </p>
        </div>
      ) : (
        <div>
          <p>Вы успешно вошли в систему!</p>
          <button onClick={handleLogout}>Выйти</button>
          <button onClick={handleViewStats}>Посмотреть статистику</button>
        </div>
      )}
    </div>
  );
};

export default AuthContainer;