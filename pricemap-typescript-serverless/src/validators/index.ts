export class ValidationError extends Error {
  constructor(violationMessage: string) {
    super(violationMessage);
  }
}
