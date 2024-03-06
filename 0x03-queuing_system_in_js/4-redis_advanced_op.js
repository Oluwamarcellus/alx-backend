import redis from "redis";
import util from "util";

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on("connect", async () => {
  client.hset("HolbertonSchools", "Portland", 50, redis.print);
  client.hset("HolbertonSchools", "Seattle", 80, redis.print);
  client.hset("HolbertonSchools", "New York", 20, redis.print);
  client.hset("HolbertonSchools", "Bogota", 20, redis.print);
  client.hset("HolbertonSchools", "Cali", 40, redis.print);
  client.hset("HolbertonSchools", "Paris", 2, redis.print);

  client.hgetall("HolbertonSchools", (error, data) => {
    if (error) console.error(error.message);
    else console.log(data);
  });
});

client.on("error", (error) => {
  console.error(error.message);
});
