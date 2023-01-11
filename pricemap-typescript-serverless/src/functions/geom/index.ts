import { handlerPath } from '@libs/handler-resolver';
import type { AWSFunction } from "../types"

export const geom: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.main`,
  events: [
    {
      http: {
        method: 'GET',
        path: '/geoms'
      },
    },
  ],
};
