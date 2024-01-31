import React from 'react';
import NotificationStats from '../components/NotificationStats'; // Путь до компонента статистики уведомлений

const AdminDashboardPage: React.FC = () => {
  return (
    <div>
      <h1>Мини-дашборд (для администратора)</h1>
      <NotificationStats />
    </div>
  );
};

export default AdminDashboardPage;
