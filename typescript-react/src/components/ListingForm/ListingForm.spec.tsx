import { render } from '@testing-library/react';
import { describe, it } from 'vitest';

import ListingForm from '.';

describe('<ListingForm />', () => {
  it('Should render the listing form component', () => {
    render(<ListingForm />);
  });
});
