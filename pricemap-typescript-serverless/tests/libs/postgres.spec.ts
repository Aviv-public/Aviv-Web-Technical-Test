import { describe, it, expect } from "vitest";
import { extractVariables } from "@/libs/postgres";

describe("extractVariables", () => {
  it("it turns an object to column names, variable indices and values", () => {
    const myTableRow = {
      id: 1,
      first_name: "Michel",
      last_name: "Dupont",
    };

    const { columns, variables, values } = extractVariables(myTableRow);

    expect(columns).toEqual(["id", "first_name", "last_name"]);
    expect(variables).toEqual(["$1", "$2", "$3"]);
    expect(values).toEqual([1, "Michel", "Dupont"]);
  });
});
