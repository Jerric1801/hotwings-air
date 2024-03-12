package com.hotwings.user.models;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "user")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class User {
    @Id
    private String userid;
    private String name;
    private String email;
    private String password;
    private int loyalty_points;
    private Object past_bookings;
    private Object upcoming_bookings;
}