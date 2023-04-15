package service

import (
	"context"
	"net"
	"testing"

	"github.com/stretchr/testify/require"
	"google.golang.org/grpc"

	"github.com/sfortson/random-scripts/src/go/grpc/pcbook/sample"
	"github.com/sfortson/random-scripts/src/go/grpc/pcbook/serializer"

	pb "github.com/sfortson/random-scripts/go/grpc/pcbook/proto"
)

func startTestLaptopServer(t *testing.T, laptopStore LaptopStore) string {
	laptopServer := NewLaptopServer(laptopStore)

	grpcServer := grpc.NewServer()
	pb.RegisterLaptopServiceServer(grpcServer, laptopServer)

	listener, err := net.Listen("tcp", ":0") // random available port
	require.NoError(t, err)

	go grpcServer.Serve(listener)

	return listener.Addr().String()
}

func newTestLaptopClient(t *testing.T, serverAddress string) pb.LaptopServiceClient {
	conn, err := grpc.Dial(serverAddress, grpc.WithInsecure())
	require.NoError(t, err)
	return pb.NewLaptopServiceClient(conn)
}

func TestClientCreateLaptop(t *testing.T) {
	t.Parallel()

	laptopStore := NewInMemoryLaptopStore()
	serverAddress := startTestLaptopServer(t, laptopStore)
	laptopClient := newTestLaptopClient(t, serverAddress)

	laptop := sample.NewLaptop()
	expectedID := laptop.Id
	req := &pb.CreateLaptopRequest{
		Laptop: laptop,
	}

	res, err := laptopClient.CreateLaptop(context.Background(), req)
	require.NoError(t, err)
	require.NotNil(t, res)
	require.Equal(t, expectedID, res.Id)

	// check that the laptop is saved to the store
	other, err := laptopStore.Find(res.Id)
	require.NoError(t, err)
	require.NotNil(t, other)

	// check that the saved laptop is the same as the one we send
	requireSameLaptop(t, laptop, other)
}

func requireSameLaptop(t *testing.T, laptop1 *pb.Laptop, laptop2 *pb.Laptop) {
	json1, err := serializer.ProtobufToJSON(laptop1)
	require.NoError(t, err)

	json2, err := serializer.ProtobufToJSON(laptop2)
	require.NoError(t, err)

	require.Equal(t, json1, json2)
}
