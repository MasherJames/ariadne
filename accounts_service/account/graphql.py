from os.path import dirname, join
from ariadne import (MutationType, QueryType,
                     make_executable_schema, ObjectType,
                     snake_case_fallback_resolvers, load_schema_from_path)
from .resolvers import resolve_create_user, resolve_get_users
from ariadne_extensions import federation


# type_defs = load_schema_from_path("./account/schema.graphql")

query_type = QueryType()
mutation = MutationType()

manager = federation.FederatedManager(
    schema_sdl_file=join(dirname(__file__), 'schema.graphql'),
    query=query_type)

user_type = ObjectType("User")

query_type.set_field("users", resolve_get_users)

mutation.set_field("createUser", resolve_create_user)

manager.add_types(user_type, mutation, query_type)
manager.add_types(snake_case_fallback_resolvers)
schema = manager.get_schema()
# schema = make_executable_schema(type_defs, [query, mutation])
