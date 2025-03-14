import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100000 },
    { duration: '5m', target: 1000000 },
    { duration: '2m', target: 0 }
  ],
}; 