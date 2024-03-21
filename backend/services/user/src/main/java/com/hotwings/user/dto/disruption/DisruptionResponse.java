package com.hotwings.user.dto.disruption;

import com.hotwings.user.models.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class DisruptionResponse {
    private List<User> user_emails;
}
