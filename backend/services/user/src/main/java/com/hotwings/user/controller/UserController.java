package com.hotwings.user.controller;

import com.hotwings.user.dto.amqp.ErrorMessage;
import com.hotwings.user.dto.amqp.NotificationsMessage;
import com.hotwings.user.dto.disruption.DisruptionRequest;
import com.hotwings.user.dto.points.PointsRequest;
import com.hotwings.user.dto.points.PointsResponse;
import com.hotwings.user.dto.user.AuthResponse;
import com.hotwings.user.dto.user.LoginRequest;
import com.hotwings.user.dto.user.UserRequest;
import com.hotwings.user.dto.user.UserResponse;
import com.hotwings.user.models.User;
import com.hotwings.user.publisher.RabbitMQProducer;
import com.hotwings.user.services.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
@CrossOrigin
public class UserController {

    private final UserService userService;
    private final RabbitMQProducer producer;

    @PostMapping("/error")
    @ResponseStatus(HttpStatus.OK)
    public ResponseEntity<String> sendError(@RequestBody ErrorMessage errorMessage) {
        producer.sendError(errorMessage);
        return ResponseEntity.ok("Message sent to RabbitMQ ...");
    }

    @PostMapping("/notifications")
    @ResponseStatus(HttpStatus.OK)
    public ResponseEntity<String> sendNotifications(@RequestBody NotificationsMessage notificationsMessage) {
        producer.sendNotifications(notificationsMessage);
        return ResponseEntity.ok("Message sent to RabbitMQ ...");
    }

    @PostMapping("/signup")
    @ResponseStatus(HttpStatus.CREATED)
    public AuthResponse createUser(@RequestBody UserRequest userRequest) {
        return userService.createUser(userRequest);
    }

    @GetMapping("/{email}")
    @ResponseStatus(HttpStatus.OK)
    public UserResponse getUserByEmail(@PathVariable String email) {
        return userService.getUser(email);
    }

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    public List<UserResponse> getAllUsers() {
        return userService.getAllUsers();
    }

    @PostMapping("/login")
    @ResponseStatus(HttpStatus.OK)
    public AuthResponse userLogin(@RequestBody LoginRequest loginRequest) {
        return userService.userLogin(loginRequest);
    }

    @PostMapping("/{email}/points")
    @ResponseStatus(HttpStatus.OK)
    public PointsResponse updateLoyaltyPoints(@PathVariable String email, @RequestBody PointsRequest pointsRequest) {
        return userService.updateLoyaltyPoints(email, pointsRequest);
    }

    @PostMapping("/disruption")
    @ResponseStatus(HttpStatus.OK)
    public List<User> getAffectedUsers(@RequestBody DisruptionRequest disruptionRequest) {
        return userService.getAffectedUsers(disruptionRequest);
    }

}
