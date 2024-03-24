package com.hotwings.user.services;

import com.hotwings.user.dto.LoginRequest;
import com.hotwings.user.dto.AuthResponse;
import com.hotwings.user.dto.UserRequest;
import com.hotwings.user.dto.UserResponse;
import com.hotwings.user.models.User;
import com.hotwings.user.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class UserService {

    private final UserRepository userRepository;

    public AuthResponse createUser(UserRequest userRequest) {
        Optional<User> checkUser = userRepository.findOneByEmail(userRequest.getEmail());
        if (checkUser.isPresent()) {
           return new AuthResponse("User already exists", false);
        } else {
            User user = User.builder()
                    .name(userRequest.getName())
                    .email(userRequest.getEmail())
                    .password(userRequest.getPassword())
                    .loyalty_points(userRequest.getLoyalty_points())
                    .past_bookings(userRequest.getPast_bookings())
                    .upcoming_bookings(userRequest.getUpcoming_bookings())
                    .build();

            userRepository.save(user);
            return new AuthResponse("Sign up successful", true);
        }
    }

    public List<UserResponse> getAllUsers() {
        List<User> users = userRepository.findAll();

        return users.stream().map(this::mapToUserResponse).toList();
    }

    private UserResponse mapToUserResponse(User user) {
        return UserResponse.builder()
                .userid(user.getUserid())
                .name(user.getName())
                .email(user.getEmail())
                .password(user.getPassword())
                .loyalty_points(user.getLoyalty_points())
                .past_bookings(user.getPast_bookings())
                .upcoming_bookings(user.getUpcoming_bookings())
                .build();
    }

    public AuthResponse userLogin(LoginRequest loginRequest) {
        String msg = "";
        String password = loginRequest.getPassword();
        Optional<User> user = userRepository.findOneByEmailAndPassword(loginRequest.getEmail(), loginRequest.getPassword());
        if (user.isPresent()) {
            return new AuthResponse("Login Success", true);
        } else {
            return new AuthResponse("Login Failed", false);
        }
    }

}
