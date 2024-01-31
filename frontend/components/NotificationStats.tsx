import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NotificationStats = () => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get('/api/notification/stats');
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching notification stats:', error);
    }
  };

  return (
    <div>
      <h2>Статистика уведомлений</h2>
      {stats ? (
        <div>
          <p>Количество информационных уведомлений: {stats.informational_count}</p>
          <p>Количество предупреждающих уведомлений: {stats.warning_count}</p>
          <p>Количество уведомлений об ошибках: {stats.error_count}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default NotificationStats;