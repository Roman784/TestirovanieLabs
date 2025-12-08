import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  // Сценарий 1: 10 пользователей на 30 секунд
  /*stages: [
    { duration: '10s', target: 10 },
    { duration: '30s', target: 10 },
    { duration: '5s', target: 0 },
  ],*/
  
  // Сценарий 2: 50 пользователей на 30 секунд
  stages: [
    { duration: '5s', target: 50 },
    { duration: '10s', target: 50 },
    { duration: '5s', target: 0 },
  ],
  
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
  },
};

export default function () {
  const response = http.get('https://httpbin.test.k6.io/get');
  
  check(response, {
    'Статус 200': (r) => r.status === 200,
    'Время ответа < 500мс': (r) => r.timings.duration < 500,
  });
  
  sleep(1);
}