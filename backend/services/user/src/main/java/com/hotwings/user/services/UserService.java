package com.hotwings.user.services;

import com.hotwings.user.dto.disruption.DisruptionRequest;
import com.hotwings.user.dto.points.PointsRequest;
import com.hotwings.user.dto.points.PointsResponse;
import com.hotwings.user.dto.user.AuthResponse;
import com.hotwings.user.dto.user.LoginRequest;
import com.hotwings.user.dto.user.UserRequest;
import com.hotwings.user.dto.user.UserResponse;
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
        }
        User user = User.builder()
                .name(userRequest.getName())
                .email(userRequest.getEmail())
                .password(userRequest.getPassword())
                .loyalty_points(userRequest.getLoyalty_points())
                .past_bookings(userRequest.getPast_bookings())
                .upcoming_bookings(userRequest.getUpcoming_bookings())
                .build();
        userRepository.save(user);
        return new AuthResponse("Registration successful", true);
    }

    public UserResponse getUser(String email) {
        User user = userRepository.findOneByEmail(email).orElse(null);
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
        Optional<User> checkUser = userRepository.findOneByEmailAndPassword(loginRequest.getEmail(), loginRequest.getPassword());
        if (checkUser.isPresent()) {
            return new AuthResponse("Login Success", true);
        }
        return new AuthResponse("Login Failed", false);
    }

    public PointsResponse updateLoyaltyPoints(String email, PointsRequest pointsRequest) {
        User user = userRepository.findOneByEmail(email).orElse(null);
        int currentPoints = user.getLoyalty_points();
        int newPoints = currentPoints + pointsRequest.getLoyalty_points();
        if (newPoints >= 0) {
            user.setLoyalty_points(newPoints);
            userRepository.save(user);
            return new PointsResponse(user.getLoyalty_points(), "Points updated successfully", true);
        }
        return new PointsResponse(currentPoints, "Points cannot be negative", false);
    }

    public List<User> getAffectedUsers(DisruptionRequest disruptionRequest) {
        String date = disruptionRequest.getDate();
        String flight_id = disruptionRequest.getFlight_id();
        return userRepository.findByDisruptedFlight(date, flight_id);
    }

}
