from os.path import dirname, join
from ariadne import (MutationType, QueryType,
                     make_executable_schema, ObjectType,
                     snake_case_fallback_resolvers, load_schema_from_path)
from .resolvers import resolve_create_review, resolve_get_reviews
from ariadne_extensions import federation


# type_defs = load_schema_from_path("./review/schema.graphql")

query_type = QueryType()
mutation = MutationType()

manager = federation.FederatedManager(
    schema_sdl_file=join(dirname(__file__), 'schema.graphql'),
    query=query_type)

user_type = federation.FederatedObjectType('User')
product_type = federation.FederatedObjectType('Product')
review_type = ObjectType('Review')


query_type.set_field("reviews", resolve_get_reviews)
mutation.set_field("createReview", resolve_create_review)

manager.add_types(user_type, product_type, review_type, mutation, query_type)
manager.add_types(snake_case_fallback_resolvers)
schema = manager.get_schema()

# schema = make_executable_schema(type_defs, [query, mutation])
