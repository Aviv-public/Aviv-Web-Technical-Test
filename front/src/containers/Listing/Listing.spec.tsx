import { render } from '@testing-library/react';
import Listing from './Listing';

describe('<Listing /> test suite', () => {
  it('Should render the Listing component', () => {
    render(<Listing />);
  });
});
