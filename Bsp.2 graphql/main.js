const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLInt } = require('graphql');

// 1. Definiere die GraphQL-Typen
const RootQueryType = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    // Einfache Abfrage, die einen Namen zurückgibt
    greeting: {
      type: GraphQLString,
      resolve: () => {
        return 'Hallo, GraphQL!';
      }
    },
    // Einfache Abfrage, die eine Zahl zurückgibt
    addNumbers: {
      type: GraphQLInt,
      args: {
        num1: { type: GraphQLInt },
        num2: { type: GraphQLInt }
      },
      resolve: (parent, args) => {
        return args.num1 + args.num2;
      }
    }
  }
});

// 2. Erstelle das Schema
const MutationType = new GraphQLObjectType({
  name: 'Mutation',
  fields: {
    // Mutation zum Ändern eines Namens (simuliert)
    setName: {
      type: GraphQLString,
      args: {
        name: { type: GraphQLString }
      },
      resolve: (parent, args) => {
        return `Der Name wurde auf ${args.name} gesetzt.`;
      }
    }
  }
});

// 3. Erstelle das vollständige Schema
const schema = new GraphQLSchema({
  query: RootQueryType,
  mutation: MutationType
});

// 4. Initialisiere Express und GraphQL
const app = express();

// Setze den GraphQL-Endpoint
app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true, // Dies ermöglicht die GraphiQL-Oberfläche zur Abfrage
}));

// Starte den Server
app.listen(4000, () => {
  console.log('Server läuft auf http://localhost:4000/graphql');
});