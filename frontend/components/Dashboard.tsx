import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [statistics, setStatistics] = useState(null);
  const [period, setPeriod] = useState('hour');

  useEffect(() => {
    // Здесть я ещё не успел разобраться как делать правильный запрос с фронта, чтобы корректно работал код
    fetchStatistics(period);
  }, [period]);

  const fetchStatistics = async (selectedPeriod) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/statistics/?period=${selectedPeriod}`);
      if (!response.ok) {
        throw new Error('Ошибка при получении статистики');
      }
      const data = await response.json();
      setStatistics(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChangePeriod = (e) => {
    setPeriod(e.target.value);
  };

  return (
    <div>
      <h2>Мини-Дашборд</h2>
      <div>
        <label htmlFor="period">Выберите период:</label>
        <select id="period" value={period} onChange={handleChangePeriod}>
          <option value="hour">За последний час</option>
          <option value="today">Сегодня</option>
          <option value="yesterday">Вчера</option>
          <option value="week">За последнюю неделю</option>
          <option value="month">За последний месяц</option>
        </select>
      </div>
      <div>
        {statistics ? (
          <ul>
            <li>Количество информационных сообщений: {statistics.informational_count}</li>
            <li>Количество предупреждающих сообщений: {statistics.warning_count}</li>
            <li>Количество сообщений об ошибках: {statistics.error_count}</li>
          </ul>
        ) : (
          <p>Загрузка статистики...</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;