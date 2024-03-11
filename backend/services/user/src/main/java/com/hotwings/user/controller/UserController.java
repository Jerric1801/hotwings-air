package com.hotwings.user.controller;

import com.hotwings.user.dto.LoginRequest;
import com.hotwings.user.dto.AuthResponse;
import com.hotwings.user.dto.UserRequest;
import com.hotwings.user.dto.UserResponse;
import com.hotwings.user.services.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
@CrossOrigin
public class UserController {

    private final UserService userService;

    @PostMapping("/signup")
    @ResponseStatus(HttpStatus.CREATED)
    public AuthResponse createUser(@RequestBody UserRequest userRequest) {
        return userService.createUser(userRequest);
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

}
