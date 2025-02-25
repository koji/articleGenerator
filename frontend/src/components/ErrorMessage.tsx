import React from 'react';

interface ErrorMessageProps {
  message: string;
}

export const ErrorMessage: React.FC<ErrorMessageProps> = ({ message }) => {
  return <p style={{ color: 'red', padding: '20px' }}>{message}</p>;
};


