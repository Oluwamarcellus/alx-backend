import redis from "redis";
import util from 'util';

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on("connect", async () => {
  console.log("Redis client connected to the server");

  const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
  };

  const displaySchoolValue = async (schoolName) => {
    try {
      const result = await getAsync(schoolName);
      console.log(result);
    } catch (error) {
      console.error(`Error getting value for ${schoolName}: ${error.message}`);
    }
  };

  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
});

client.on("error", (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});
