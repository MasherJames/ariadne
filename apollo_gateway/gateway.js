const { ApolloServer } = require("apollo-server");
const { ApolloGateway } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  serviceList: [
    {
      name: "accounts",
      url: "http://localhost:8000/graphql/"
    },
    {
      name: "products",
      url: "http://127.0.0.1:8001/graphql/"
    },
    {
      name: "reviews",
      url: "http://127.0.0.1:8002/graphql/"
    }
  ]
});

const init = async () => {
  let gatewayConfig;

  try {
    gatewayConfig = await gateway.load();
  } catch (error) {
    console.log(error);
    return null;
  }

  const server = new ApolloServer({
    ...gatewayConfig
  });
  server.listen().then(({ url }) => {
    console.log(`Server ready at ${url}`);
  });
};
init();
