import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { CSSTransition, TransitionGroup } from 'react-transition-group';

const NotificationSystem = ({ addNotification }) => {
  const [notifications, setNotifications] = useState([]);

  const handleAddNotification = (message, type) => {
    const newNotification = { message, type, timestamp: Date.now() };
    setNotifications([...notifications, newNotification]);
    setTimeout(() => {
      setNotifications(notifications.filter(n => n !== newNotification));
    }, 5000);
  };

  return (
    <div>
      <button onClick={() => handleAddNotification('This is a success message', 'success')}>
        Add Success Notification
      </button>
      <button onClick={() => handleAddNotification('This is a warning message', 'warning')}>
        Add Warning Notification
      </button>
      <button onClick={() => handleAddNotification('This is an error message', 'error')}>
        Add Error Notification
      </button>
      <TransitionGroup>
        {notifications.map((notification, index) => (
          <CSSTransition key={index} timeout={500} classNames="notification">
            <div className={`notification-${notification.type}`}>
              {notification.message}
            </div>
          </CSSTransition>
        ))}
      </TransitionGroup>
    </div>
  );
};

NotificationSystem.propTypes = {
  addNotification: PropTypes.func.isRequired,
};

export default NotificationSystem;