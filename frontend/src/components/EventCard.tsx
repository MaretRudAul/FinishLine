import React from "react"
import { EventCardData } from "../types";


const EventCard: React.FC<EventCardData> = ({
  title, host, location, description, datetime, pictureUrl, tag, websiteOrigin, link
}) => {
  return (
    <a
      href={link}

      className="flex items-center justify-center flex-col flex-grow
    h-full w-full sm:w-80 md:w-96 lg:w-1/3 xl:w-1/4 p-4 sm:p-6 md:p-8 text-lg sm:text-xl md:text-2xl gap-4 mb-4 minHeight:400px
    transform transition-transform duration-300 hover:scale-105
    border border-gray-300 bg-red-100 rounded-md wrap:wrap ">
      <div>

        {/* Title */}
        <div className="mb-2">
          <h2 className="text-2xl font-bold text-gray-800 text-center ml-4 mr-4 font-sans italic tracking-wide">{title}</h2>
        </div>

        {/* Picture */}
        <div className="w-full h-48 object-cover rounded-md mb-12">
          <img src={pictureUrl} />
        </div>

        {/* Description */}
        <div className="mb-2">
          <p className="text-gray-700 ml-4 mr-4">{description}</p>
        </div>

        {/* Host */}
        <div className="mb-2">
          <p className="text-gray-700 ml-4 mr-4">
            <strong></strong> {host}
          </p>
        </div>

        {/* Location */}
        <div className="mb-2">
          <p className="text-gray-700 ml-4 mr-4">
            <strong></strong> {location}
          </p>
        </div>

        {/* Date and Time */}
        <div className="mb-2">
          <p className="text-gray-700 ml-4 mr-4 sm:text-sm">
            <strong></strong> {datetime}, {datetime}
          </p>
        </div>

        {/* Website Origin 
      <div className="mb-2">
        <p className="text-gray-700 ml-4 mr-4">
          <strong>Website:</strong> {websiteOrigin}
        </p>
      </div>  */}

      </div>
    </a>
  )

};


// Tags moved out of here
// {/* Tags */}
// {tag.length > 0 && (
//   <div className="mt-4 flex flex-wrap gap-2 ml-4 mr-4">
//     {tag.map((item, index) => (
//       <span
//         key={index}
//         className="inline-block bg-gray-200 text-gray-700 text-sm px-3 py-1 rounded-full"
//       >
//         {item}
//       </span>
//     ))}
//   </div>
// )}

export default EventCard;
