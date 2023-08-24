import { render } from '@testing-library/react';
import { describe, it } from 'vitest';

import PricesHistory from './PricesHistory';

describe('<PricesHistory /> test suite', () => {
  it('Should render the <PricesHistory /> component', () => {
    render(<PricesHistory />);
  });
});
