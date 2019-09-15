from os.path import dirname, join
from ariadne import (MutationType, QueryType,
                     make_executable_schema, load_schema_from_path, ObjectType,
                     snake_case_fallback_resolvers)
from .resolvers import resolve_create_product, resolve_get_products
from ariadne_extensions import federation


# type_defs = load_schema_from_path("./product/schema.graphql")

query_type = QueryType()
mutation = MutationType()

manager = federation.FederatedManager(
    schema_sdl_file=join(dirname(__file__), 'schema.graphql'),
    query=query_type)

product_type = ObjectType("Product")
query_type.set_field("products", resolve_get_products)
mutation.set_field("createProduct", resolve_create_product)

manager.add_types(product_type, mutation, query_type)
manager.add_types(snake_case_fallback_resolvers)
schema = manager.get_schema()

# schema = make_executable_schema(type_defs, [query, mutation])
