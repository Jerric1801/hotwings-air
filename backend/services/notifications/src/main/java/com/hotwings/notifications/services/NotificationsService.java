package com.hotwings.notifications.services;

import com.hotwings.notifications.dto.NotificationsMessage;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class NotificationsService {

    private final EmailSenderService senderService;

    public void sendUserEmail(NotificationsMessage notificationsMessage) {
        String email = notificationsMessage.getEmail();
        String type = notificationsMessage.getNotification_type();
        String msg = notificationsMessage.getNotification_message();
        senderService.sendEmail(email, type, msg);
    }
}
