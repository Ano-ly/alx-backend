import { createClient } from 'redis';

// Wrap your code inside an IIFE
(async () => {
    const myClient = createClient();
    
    myClient.on('error', (err) => {
        console.log('Redis Client Error', err);
    });

    await myClient.connect();

    // Use the client for your operations
    await myClient.set('key', 'value');
    const value = await myClient.get('key');
    console.log(value);

    // Close the client when done
    await myClient.quit();
})();
