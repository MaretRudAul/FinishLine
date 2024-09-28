import React from "react"

interface HeaderProps {
  title: string;
  host: string;
  location: string;
  description: string;
  datetime: Date;
  pictureUrl: string;
  tag: string[];
  websiteOrigin: string;
  link: string;
}

const EventCard: React.FC<HeaderProps> = ({
  title, host, location, description, datetime, pictureUrl, tag, websiteOrigin, link
}) => {
  return (
    <div>
      <p>
        {`
      ${title}
      ${host}
      ${location}
      ${description}
      ${datetime}
      ${link}
      ${websiteOrigin}
      ${tag}
      ${pictureUrl}
        `}
      </p>
    </div>
  )

}

export default EventCard;
