import { render } from '@testing-library/react';
import { describe, it } from 'vitest';

import Listings from './Listings';

describe('<Listings /> test suite', () => {
  it('Should render the <Listings /> component', () => {
    render(<Listings />);
  });
});
