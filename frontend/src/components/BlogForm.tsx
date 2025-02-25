import { useState, FormEvent } from 'react';

interface BlogFormProps {
  onSubmit: (topic: string) => void;
}

export const BlogForm: React.FC<BlogFormProps> = ({ onSubmit }) => {
  const [topic, setTopic] = useState<string>('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (topic.trim()) {
      onSubmit(topic);
      setTopic(''); // Clear input after submission
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter a topic"
      />
      <button type="submit" disabled={!topic.trim()}>
        Generate
      </button>
    </form>
  );
};

