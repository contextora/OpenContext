export const OpenContextAgent = {
  version: '1.0',
  description: 'AI Agent for the OpenContext Protocol',
  routes: {
    "/ask": async ({ question }) => {
      return `You asked: ${question}. Response powered by OpenContext.`;
    }
  }
};
