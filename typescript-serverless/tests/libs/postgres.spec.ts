import { describe, it, expect } from "vitest";
import { extractVariables } from "@/libs/postgres";

describe("extractVariables", () => {
  it("it turns an object to column names, variable indices and values", () => {
    const myTableRow = {
      id: 1,
      first_name: "Michel",
      last_name: "Dupont",
    };

    const extracted = extractVariables(myTableRow);

    expect(extracted).toEqual({
      columns: ["id", "first_name", "last_name"],
      variables: ["$1", "$2", "$3"],
      columnsVariables: ["id = $1", "first_name = $2", "last_name = $3"],
      values: [1, "Michel", "Dupont"],
    });
  });
});
