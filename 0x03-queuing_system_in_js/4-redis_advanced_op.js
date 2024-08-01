import { createClient } from 'redis';
import { print } from 'redis';

const myClient = createClient();

myClient
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

myClient.connect();

function setNewSchool(schoolName, value) {
  myClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  myClient.get(schoolName, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      console.log(result);
    }
  });
}

myClient.on('connect', () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});
