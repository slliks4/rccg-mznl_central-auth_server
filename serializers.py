# PASSWORD CHANGE SERIALIZER
# class PasswordChangeSerializer(serializers.Serializer):
#     old_password = serializers.CharField(write_only=True, required=True)
#     new_password = serializers.CharField(write_only=True, required=True)
#     confirm_password = serializers.CharField(write_only=True, required=True)
# 
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         # Djano default function for checking password
#         if not user.check_password(value):
#             raise serializers.ValidationError("Current password is incorrect.")
#         return value
# 
#     def validate(self, attrs):
#         if attrs['new_password'] != attrs['confirm_password']:
#             raise serializers.ValidationError({
#                 "confirm_password": "Does not match new password."
#             })
#         try:
#             validate_password(
#                 attrs['new_password'], self.context['request'].user
#             )
#         except DjangoValidationError as e:
#             raise serializers.ValidationError({"new_password": e.messages})
#         return attrs
# 
#     def save(self, **kwargs):
#         user = self.context['request'].user
#         user.set_password(self.validated_data['new_password'])
#         user.save()
#         return user
