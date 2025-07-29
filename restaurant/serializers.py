from rest_framework import serializers
from .models import MenuItem, Table, Reservation, Order, InventoryItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source='table', write_only=True
    )

    class Meta:
        model = Reservation
        fields = ['id', 'customer_name', 'reservation_date', 'reservation_time', 'guests', 'table', 'table_id']


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source='table', write_only=True
    )
    items = MenuItemSerializer(many=True, read_only=True)
    item_ids = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), many=True, source='items', write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'table', 'table_id', 'items', 'item_ids', 'created_at']


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
