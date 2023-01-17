#!/usr/bin/env node

const path = require("path");
const fs = require("fs");
const { parse } = require("yaml");
const { compile } = require("json-schema-to-typescript");

const schemasPath = path.join(__dirname, "../../schemas/listingsapi.yaml");
const generatedTypesPath = path.join(__dirname, "../src/types.generated.d.ts");

const openAPISchemaYaml = fs.readFileSync(schemasPath, "utf8");
const openAPISchema = parse(openAPISchemaYaml);

// Copy schemas to `definitions` to be picked by types generator
const jsonSchemaDefinitions = "definitions";
openAPISchema[jsonSchemaDefinitions] = openAPISchema["components"]["schemas"];

compile(openAPISchema, "APISchemas", {
  unreachableDefinitions: true,
}).then((ts) => fs.writeFileSync(generatedTypesPath, ts));
