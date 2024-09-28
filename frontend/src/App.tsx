import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import EventCard from './components/EventCard';

function App() {
  const mockupData = {
    title: "Title",
    host: "Host",
    location: "Place",
    description: "Lorem Ipsum",
    datetime: new Date(),
    link: "https://sugma.com",
    websiteOrigin: 'Sugma',
    tag: ['tag1', 'tag2'],
    pictureUrl: "picture"
  };
  const apiData = [mockupData, mockupData, mockupData];
  return (
    <div className="">
      <Header />
      {apiData.map((data) => (
        <EventCard
          title={data.title}
          host={data.host}
          location={data.location}
          description={data.description}
          datetime={data.datetime}
          link={data.link}
          websiteOrigin={data.websiteOrigin}
          tag={data.tag}
          pictureUrl={data.pictureUrl}
        />
      )
      )}
    </div>
  );
}

export default App;
