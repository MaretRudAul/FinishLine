import React, { useEffect, useState } from 'react';
import './App.css';
import Header from './components/Header';
import EventCard from './components/EventCard';
import { EventCardData } from './types';

function App() {
  // const mockupData = {
  //   title: "Title",
  //   host: "Host",
  //   location: "Place",
  //   description: "Lorem Ipsum",
  //   datetime: new Date(),
  //   link: "https://google.com",
  //   websiteOrigin: 'Sugma',
  //   tag: ['tag1', 'tag2'],
  //   pictureUrl: "https://static.campuslabsengage.com/discovery/images/events/social.jpg"
  // };
  // const apiData = [mockupData, mockupData, mockupData,mockupData, mockupData, mockupData,mockupData, mockupData, mockupData,mockupData, mockupData, mockupData];
  //
  const [events, setEvents] = useState<EventCardData[]>([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/fetch-events')
      .then(response => response.json())
      .then(data => setEvents(data));
  }, []);

  return (
    <div>
      <Header />
      <div className="flex justify-center items-center flex-wrap gap-4 mt-5">
        {events.map((data) => (
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
    </div>
  );
}

export default App;
