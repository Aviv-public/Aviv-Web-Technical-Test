export const getFormattedDate = (rawDate: Date): string => {
  if (!rawDate) {
    return '';
  }
  const readableDate = new Date(rawDate);

  return readableDate.toISOString()?.split('T')[0];
};
