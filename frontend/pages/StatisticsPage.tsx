import React, { useEffect, useState } from 'react';

const StatisticsPage: React.FC = () => {
  const [statistics, setStatistics] = useState<any>(null);

  useEffect(() => {
    // Очевидно зедсь нужно передавать запрос, но я не успел
  }, []);

  return (
    <div>
      <h1>Статистика</h1>
      {statistics ? (
        <div>
          <p>Информационные сообщения: {statistics.informational_count}</p>
          <p>Предупреждающие сообщения: {statistics.warning_count}</p>
          <p>Сообщения об ошибках: {statistics.error_count}</p>
        </div>
      ) : (
        <p>Загрузка статистики...</p>
      )}
    </div>
  );
};

export default StatisticsPage;