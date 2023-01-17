import { Listing } from "src/types.generated";
// import { ValidationError } from ".";

export function validateListing(listing: unknown): asserts listing is Listing {
  // if (!isNameValid(listing.name)) {
  //     throw new ValidationError("dssd")
  // }
}

// function isNameValid(name: unknown): name is string {
//     return typeof name === "string"
// }
