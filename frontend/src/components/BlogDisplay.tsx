import React from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeHighlight from 'rehype-highlight';

interface BlogDisplayProps {
  content: string;
}

export const BlogDisplay: React.FC<BlogDisplayProps> = ({ content }) => {
  return (
    <div className="markdown-body">
      <ReactMarkdown rehypePlugins={[rehypeHighlight]}>{content}</ReactMarkdown>
    </div>
  );
};


