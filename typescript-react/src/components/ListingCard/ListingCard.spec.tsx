import { render } from '@testing-library/react';
import { describe, it } from 'vitest';

import ListingCard from './ListingCard';

describe('<ListingCard /> test suite', () => {
  it('Should render the <ListingCard /> component', () => {
    render(<ListingCard />);
  });
});
