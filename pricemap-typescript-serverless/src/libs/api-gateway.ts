export const formatJSONResponse = (response: object, statusCode = 200) => {
  return {
    statusCode,
    body: JSON.stringify(response)
  }
}
