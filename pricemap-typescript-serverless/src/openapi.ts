import { join } from "path";
import { readFileSync } from "fs";
import { parse } from "yaml";

const schemasPath = join(__dirname, "../../schemas/listingsapi.yaml");
const openAPISchemaYaml = readFileSync(schemasPath, "utf8");
const listingsAPISchema = parse(openAPISchemaYaml);

function appendDefinitionsToSchema(schema: object) {
  const schemaWithDefinitions = {
    ...schema,
    components: { schemas: listingsAPISchema["components"]["schemas"] },
  };

  return schemaWithDefinitions;
}

export function getRequestBodySchema(method: string, path: string) {
  const pathDefinitions = listingsAPISchema["paths"];
  if (!(path in pathDefinitions)) {
    throw new Error(`Missing path ${path} in paths list`);
  }

  const pathDefinition = pathDefinitions[path];
  if (!(method in pathDefinition)) {
    throw new Error(`Missing method ${method} in path definition of ${path}`);
  }

  return appendDefinitionsToSchema(
    pathDefinition[method]["requestBody"]["content"]["application/json"][
      "schema"
    ]
  );
}
